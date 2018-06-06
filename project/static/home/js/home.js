$(document).ready(function(){
    setTimeout(function(){
        swiper1();
    },150);
    setTimeout(function(){
        swiper2();
    },200);
})



function swiper1(){
    var mySwiper1 = new Swiper('#topSwiper',{
        direction: 'horizontal',
        loop : true,
        speed : 500,
        autoplay: 2000,
        pagination: '.swiper-pagination',
        control: true,
    });
};

function swiper2(){
    var mySwiper2 = new Swiper('#swiperMenu',{
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
    });
};