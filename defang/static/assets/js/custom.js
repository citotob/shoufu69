/*
Template Name: VIDOE - Video Streaming Website HTML Template
Author: Askbootstrap
Author URI: https://themeforest.net/user/askbootstrap
Version: 1.0
*/
(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
   $(document).on('click', '#sidebarToggle', function(e) {  
    e.preventDefault();
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($window.width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });
  
  // Category Owl Carousel
  const objowlcarousel = $('.owl-carousel-category');
  if (objowlcarousel.length > 0) {
    objowlcarousel.owlCarousel({
      responsive: {
        0:{
            items:1,
        },
        600:{
            items:3,
            nav:false
        },
        1000: {
          items: 4,
        },
        1200: {
          items: 8,
        },
      },
      loop: true,
      lazyLoad: true,
      autoplay: true,
      autoplaySpeed: 1000,
      autoplayTimeout: 2000,
      autoplayHoverPause: true,
      nav: true,
      navText:["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
    });
  }

  // Login Owl Carousel
  const mainslider = $('.owl-carousel-login');
  if (mainslider.length > 0) {
    mainslider.owlCarousel({
      items: 1,
      lazyLoad: true,
      loop: true,
      autoplay: true,
      autoplaySpeed: 1000,
      autoplayTimeout: 2000,
      autoplayHoverPause: true,
    });
  }

	
  // Tooltip
  $('[data-toggle="tooltip"]').tooltip()

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    event.preventDefault();
  });

  // 'add another picture' button
  $('#add-picture').click(function(){
    var count = $("#picture-form-group > .form-group").length;
    var picNum = count + 1;
    var picElem = '<div class="form-group"><label for="pic_'+picNum+'">Choose Picture</label><input type="file" class="form-control-file" id="pic_'+picNum+'" name="pic_'+picNum+'"><label class="mt-2" for="pic_cap_'+picNum+'">Caption</label><input type="text" placeholder="caption for this picture" id="pic_cap_'+picNum+'" name="pic_cap_'+picNum+'" class="form-control"> </div>';
    if (count < 10 ) {
      $('#picture-form-group').append(picElem);
      $('#sum_pic').val(picNum);
    } else {
      $('#add-picture').hide();
    }
  })

  // aspect ratio video thumbnail
  function resize_thumbs(){
    var wd = $('.video-card-body').width();
    var hg = (wd / 16) * 9;
    $('.video-card-image img').height(hg)
  }
  
  resize_thumbs();
  $(window).resize(function(){
    resize_thumbs();
  });

  // thumbnail animation
  var timer,
  count = 0,
  cycle = function(el, root){
    count = (count+1)%21;
    var img_url = window.location.origin + root + '_' + count + '.jpg';
    $.get(img_url)
      .done(function() { 
        // console.log('berhasil');
        el.attr('src', root + '_' + ((count==0) ? '1' : count) + '.jpg');
      }).fail(function() { 
        // console.log('gagal');
        count = 0;
        el.attr('src', root + '_1.jpg')
      })
  };
  $('.video-card').hover(function(){
    var gambar = $('img', this);
    var thumbDefault = gambar.attr('thumb-default');
    var root = thumbDefault.replace('_1.jpg','');
    cycle(gambar, root);
    timer = setInterval(function(){ cycle(gambar, root); }, 150);
  }, function(){
    clearInterval(timer);
    var gambar = $('img', this);
    var thumbDefault = gambar.attr('thumb-default');
    gambar.attr('src', thumbDefault);
  });


    //change active status on menu sidebar
  function change_active_status(el) {
    $('.sidebar .side-menu').removeClass("active");
    $('.sidebar .side-menu.' + el ).addClass("active");
  }

  $(document).ready(function(){
    var current_path = window.location.pathname;
    var path_array = current_path.split('/');
    if (current_path == '/' || path_array[1] == 'videos'){
      change_active_status('video');
    } else if (path_array[1] == 'stories'){
      change_active_status('story');
    } else if (path_array[1] == 'albums') {
      change_active_status('photo');

    }
  });

})(jQuery); // End of use strict