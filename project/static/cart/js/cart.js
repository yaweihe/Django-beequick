$(document).ready(function(){


    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    for (var i = 0; i < addShoppings.length; i++) {
        addShopping = addShoppings[i]

        addShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/0/", {"productid":pid}, function(data){
                if (data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price
                }
            })
        },false)

        }
    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]

        subShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/1/", {"productid":pid}, function(data){
                if (data.status == "success"){
                //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price
                    if (data.data == 0){
                        //window.location.reload()
                        //Dom节点动态操作
                        //当选中商品在购物车中减少至0，自动删除该项
                        var li = document.getElementById(pid + "li")
                        li.parentNode.removeChild(li)
                    }
                    //document.getElementById(sid).innerHTML = data.data

                }
            })
        },false)
    }


    var ischoses = document.getElementsByClassName("ischose")
    for (var j = 0; j < ischoses.length; j++) {

        ischoses[j].addEventListener("click", function(){
            pid = this.getAttribute("goodsid")
            $.post("/changecart/2/", {"productid":pid}, function(data){
                if (data.status == "success"){
                   //window.location.href = "http://127.0.0.1:8000/cart/"
                   var s = document.getElementById(pid + "a")
                   s.innerHTML = data.data
                }
            })
        }, false)
    }



    var ok = document.getElementById("ok")
    ok.addEventListener("click",function(){
        var d = confirm("是否下单？")
        if (d){
            $.post("/saveorder/",function(){
                if(data.status = "success"){
                    window.location.href = "http://127.0.0.1/8000/cart/"
                }
            })
        }


        $.get("/saveorder/",function(data){
            if (data.status == "error"){
                console.log("订单失败")
            } else {
                console.log("订单成功")
                window.location.reload()
            }
        })
    })

})
