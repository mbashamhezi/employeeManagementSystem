// var navLinks = document.querySelectorAll("nav a");
// var contentSections = document.querySelectorAll(".content > div");

// navLinks.forEach(function(link) {
//   link.addEventListener("click", function(e) {
//     e.preventDefault();

//     var target = this.getAttribute("href").substring(1);
//     showContentSection(target);
//   });
// });

// function showContentSection(target) {
//   contentSections.forEach(function(section) {
//     section.style.display = "none";
//   });

//   var selectedSection = document.getElementById(target);
//   selectedSection.style.display = "block";
// }


        function showForm(formId) {
            var forms = document.getElementsByClassName('content')[0].getElementsByTagName('form');
            for (var i = 0; i < forms.length; i++) {
                forms[i].style.display = 'none';
            }
            document.getElementById(formId).style.display = 'block';
        }
