
        function showSection(sectionId) {
            var sections = document
                .getElementsByClassName("content")[0]
                .getElementsByTagName("section");
            for (var i = 0; i < sections.length; i++) {
                sections[i].style.display = "none";
            }
            document.getElementById(sectionId).style.display = "block";
        }
    

    $(document).ready(function() {
        var rowsPerPage = 5;
        var currentPage = 0;
        var tableRows = $('.table tbody tr');
        var totalPages = Math.ceil(tableRows.length / rowsPerPage);
        
        showPage(currentPage);
        
        $('#prev').click(function(e) {
            e.preventDefault();
            if (currentPage > 0) {
                currentPage--;
                showPage(currentPage);
            }
        });
        
        $('#next').click(function(e) {
            e.preventDefault();
            if (currentPage < totalPages - 1) {
                currentPage++;
                showPage(currentPage);
            }
        });
        
        function showPage(page) {
            tableRows.hide();
            var startIndex = page * rowsPerPage;
            var endIndex = startIndex + rowsPerPage;
            tableRows.slice(startIndex, endIndex).show();
            
            $('.pagination a').removeClass('active');
            $('.pagination a').eq(page + 1).addClass('active');
        }
    });

