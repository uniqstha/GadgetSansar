// JavaScript Code


$(document).ready(function(){
    // scroll up
// When the user scrolls down 20px from the top of the document, show the button
      
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 230 || document.documentElement.scrollTop > 230) {
     myBtn.style.display = "block"; 
    } 
  else {
     myBtn.style.display = "none";
    }
  }
                  
// When the user clicks on the button, scroll to the top of the document
           
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}  
    // //Active Scroll
    // const sections = document.querySelectorAll('section[id]');
    // window.addEventListener('scroll', scrollActive);

    // function scrollActive(){
    //     const scrollY = window.pageYOffset

    //     sections.forEach(current => {
    //         const sectionHeight = current.offsetHeight;
    //         const sectionTop = current.offsetTop - 85;
    //         sectionId = current.getAttribute('id');

    //         if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
    //             document.querySelector('.navbar-nav a[href*=' + sectionId + ']').classList.add('active')
    //         } else {
    //             document.querySelector('.navbar-nav a[href*=' + sectionId + ']').classList.remove('active')
    //         }
    //     })
    // }

  

    //Search Toggle Button
    $(function(){
        $('.toggle-overlay').click(function(){
            $('.search-overlay').toggleClass('open');
        })
    })

    //Menu Toggle Button
    $('.menu-toggle').click(function(){
        $('.menu-toggle').toggleClass('active');
    })

    //Filter Section
    // $(".gallery-button").click(function () {
    //     var name = $(this).attr('data-filter');
    //     if (name == "all") {
    //         $(".shot-thumbnail").show('2000');
    //     } else {
    //         $(".shot-thumbnail").not("." + name).hide('2000');
    //         $(".shot-thumbnail").filter("." + name).show('2000');
    //     }
    // })

    // $('.navigation a').click(function(){
    //     $(this).addClass("active").siblings().removeClass('active');
    // });



//     //owl carousel
//     $('#our-team').owlCarousel({
//         loop:true,
//         autoplay:true,
//         margin:10,
//         responsiveClass:true,
//         nav:false,
//         dots:true,
//         responsive:{
//             0:{
//                 items:1
//             },
//             600:{
//                 items:2
//             },
//             1000:{
//                 items:3
//             }
//         }
//     }) 

 })
 
//  product details
var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl)
})



function showToast(){
    toastList[0].show()
}

// Enable Tooltip
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

function goToProductDetails() {
    window.location.href = "productDetails.html";
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

// accordion js
$(document).ready(function(){
    $("#accordion .card .card-link").click(function(){
        if($(this).find("i.fa").hasClass("fa-minus"))
        {
            $(this).find("i.fa").removeClass("fa-minus");
            $(this).find("i.fa").addClass("fa-plus");
        }
        else if($(this).find("i.fa").hasClass("fa-plus"))
        {
            $(this).find("i.fa").removeClass("fa-plus");
            $(this).find("i.fa").addClass("fa-minus");

        }
        $(this).parents(".card").siblings().find(".card-header .card-link i.fa").removeClass("fa-minus");
        $(this).parents(".card").siblings().find(".card-header .card-link i.fa").addClass("fa-plus");
    })
})

// accordion end 
// img select 
var MainImg=document.getElementById('image');
var small_img=document.getElementsByClassName("smallimg");
small_img[0].onclick=function(){
    MainImg.src=small_img[0].src;
}
small_img[1].onclick=function(){
    MainImg.src=small_img[1].src;
}
small_img[2].onclick=function(){
    MainImg.src=small_img[2].src;}

// scroll up
// When the user scrolls down 20px from the top of the document, show the button
      
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 230 || document.documentElement.scrollTop > 230) {
     myBtn.style.display = "block"; 
    } 
  else {
     myBtn.style.display = "none";
    }
  }
                  
// When the user clicks on the button, scroll to the top of the document
           
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}        
// slider
$(document).ready(function() {

  $('#carousel').carousel({
  
  interval: 100
  
  })
  
  });
