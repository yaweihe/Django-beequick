$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    //var showyellow = document.getElementById("showyellow")


    typediv.style.display = "none"
    sortdiv.style.display = "none"
    //showyellow.style.display = "none"
    /*
    showyellow.addEventListener("click",function(){
        showyellow.style.display = "block"
    },false);
    */
    /*
    当点击一块区域时，左侧导航栏黄色指示亮起

    $(".yellowSlide").click(function(){
        var show = $(".yellowSlide").css('display');
        if(show == 'none'){
           $('.yellowSlide').css('display','block')
        }
        if(show == 'block'){
            $('.yellowSlide').css('display','none')
        }
    });
    */

    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)

    showsortbtn.addEventListener("click",function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)

    typediv.addEventListener("click",function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)

    sortdiv.addEventListener("click",function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"

    },false);

    //修改购物车
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]

        addShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/0/",{"productid":pid},function(data){
                if(data.status == "success"){
                    //添加成功，把中间span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                    //console.log("数量",data.data)
                }
                else{
                    if(data.data == -1){
                        /*
                        console.log("**********")
                        $.get("/login/")
                        */
                        //写死了这个连接，后续需要根据主机服务进行拼接链接
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        },false)
    }

    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]

        subShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/1/",{"productid":pid},function(data){
                if(data.status == "success"){
                    //减少成功，把中间span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data

                }
                else{
                    if(data.data == -1){
                        /*
                        console.log("**********")
                        $.get("/login/")
                        */
                        //写死了这个连接，后续需要根据主机服务进行拼接链接
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        },false)
    }
});