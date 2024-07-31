from django.shortcuts import render, redirect
from superadmin.models import Task ,Board,Task,Employee,TaskFile
from .forms import TaskForm , BoardForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required




@login_required(login_url='/superadmin/login/')
def create_task(request):
    boards = Board.objects.all()
    selected_board_id = request.GET.get('board_id')

    # Prepare initial data with board_id if provided
    initial_data = {'board': selected_board_id} if selected_board_id else None

    # Initialize the form with POST data (for form submission) or initial data (for pre-filling)
    form = TaskForm(request.POST or None, request.FILES or None, initial=initial_data)

    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Save the form data to create a new Task object
            
            messages.success(request, 'Task create successfully')
            return redirect('superadmin:kanban_board')  # Redirect after successful creation
        else:
            # Form is invalid, handle the errors
            messages.error(request, 'Please correct the errors below.')

    # If GET request or invalid form, render the form again with context
    return render(request, 'superadmin/tasks/createtask.html', {
        'form': form,
        'boards': boards,
        'selected_board_id': selected_board_id,  # Pass the selected board ID to the template for pre-selection
    })

@login_required(login_url='/superadmin/login/')
def upload_task_filess(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)

        # Check if there are files in the request
        if 'file' in request.FILES:
            # Process each file
            for file in request.FILES.getlist('file'):
                TaskFile.objects.create(task=task, file=file)  # Assuming 'file' is the correct field name
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'No files uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

    
# views.py
@login_required(login_url='/superadmin/login/')
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    boards = Board.objects.all()
    selected_board_id = task.board.id if task.board else None

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            board_id = request.POST.get('board_id')
            if board_id:
                updated_task.board = get_object_or_404(Board, pk=board_id)
            updated_task.save()
            messages.success(request, 'Client created successfully.')
            return redirect('superadmin:kanban_board')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TaskForm(instance=task)

    return render(request, 'superadmin/tasks/updatetask.html', {
        'form': form,
        'task': task,
        'boards': boards,
        'selected_board_id': selected_board_id,
    })



@login_required(login_url='/superadmin/login/')    
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        messages.warning(request, 'Task delete successfully.')
        return redirect('superadmin:kanban_board')  # Replace with your task list URL name
    
    # Optionally handle GET request for confirmation or display
    return render(request, 'superadmin/tasks/task_delete.html', {'task': task})


# views.py

@login_required
def kanban_board(request):
    boards = Board.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'boards': boards,
        'tasks': tasks,      
        'form':form
    }
    return render(request, 'superadmin/tasks/kanban_board.html', context)

@login_required(login_url='/superadmin/login/')
def add_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Board created successfully.')
            return redirect('superadmin:kanban_board')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BoardForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'superadmin/tasks/add_board.html', context)

@login_required(login_url='/superadmin/login/')
def edit_board(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            messages.success(request, 'Board updated successfully.')
            return redirect('superadmin:kanban_board')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BoardForm(instance=board)
    
    context = {
        'form': form,
    }
    
    return render(request, 'superadmin/tasks/add_board.html', context)

@login_required(login_url='/superadmin/login/')
def task_detail(request, task_id):
    # Retrieve the task object based on task_id
    task = get_object_or_404(Task, pk=task_id)
    
    # Pass the task object to the template for rendering
    context = {
        'task': task,
    }
    
    return render(request, 'superadmin/tasks/task_details.html', context)

@login_required(login_url='/superadmin/login/')
def delete_board(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        board.delete()
        return redirect('superadmin:kanban_board')
    return redirect('superadmin:kanban_board')  # or render a confirmation page

@login_required(login_url='/superadmin/login/')
@csrf_exempt
def update_task_board(request, task_id):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            new_board_id = data.get('board_id')

            if not new_board_id:
                return JsonResponse({'success': False, 'error': 'No board ID provided'})

            # Fetch the task and the new board from the database
            task = Task.objects.get(pk=task_id)
            new_board = Board.objects.get(pk=new_board_id)

            # Update the task's board and save
            task.board = new_board
            task.save()

            # Return a success response
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except Board.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Board not found'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})