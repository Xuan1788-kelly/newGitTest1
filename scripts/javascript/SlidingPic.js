$(function() {
    // configuration
    var width = 720;
    var animationSpeed = 1000;
    var pause = 3000;
    var currentSlide = 1;
    //cache DOM

    var $slider = $('#slider');
    var $slideContainer = $slider.find('.slides');
    var $slides = $slideContainer.find('.slide');

    var interval;

    function startSlider() {
        // setinverval
        interval = setInterval(function() {
            // animate margin-left
            $slideContainer.animate({"margin-left": "-="+width}, animationSpeed, function() {
                currentSlide++;
                // if it is the last slide, go to positin 1 (0px)
                if (currentSlide === $slides.length) {
                    currentSlide = 1;
                    $slideContainer.css('margin-left', 0);
                }
            });
        }, pause);
    }

    function stopSlider() {
        clearInterval(interval);
    }
    // listen for mouseenter and pause
    $slider.on('mouseenter', stopSlider).on('mouseleave', startSlider);
    // resume on mouseleave
    startSlider();

});