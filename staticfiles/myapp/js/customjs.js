// for multiselect drop down when admin add new project
$(document).ready(function() {
    $('.js-example-basic-multiple').select2({
        placeholder: "Select employees",
        allowClear: true,
        width: '100%'
    });

    // Display the selected file name in the label
    $(".custom-file-input").on("change", function() {
        var fileName = $(this).val().split("\\").pop();
        $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
    });
});


    function confirmDelete() {
        return confirm('Are you sure you want to delete this lead?');
    }

// Disable Dropzone auto-discovery






//auto search functionality for search proejct
// $(document).ready(function() {
//     $('#search-input').keyup(function() {
//         var query = $(this).val().trim(); // Get the search query
        
//         // Send AJAX request
//         $.ajax({
//             url: '/path/to/your/project_detail/',  // Update with your actual URL
//             type: 'GET',
//             data: {
//                 'q': query  // Pass the search query as 'q'
//             },
//             dataType: 'json',
//             beforeSend: function() {
//                 // Show loading spinner or do something before sending the request
//             },
//             success: function(data) {
//                 // Update the search results container with the received HTML
//                 $('#search-results').html(data.html);
//             },
//             error: function(xhr, status, error) {
//                 // Handle errors if any
//                 console.error('AJAX Error:', status, error);
//             }
//         });
//     });
// });
