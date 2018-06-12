$(document).ready(function(){
    var accunt = document.getElementById('accunt')
    var pass = document.getElementById('pass')
    var passwd = document.getElementById('passwd')

    var accunterr = document.getElementById('accunterr')
    var checkerr = document.getElementById('checkerr')
    var passerr = document.getElementById('passerr')
    var passwderr = document.getElementById('passwderr')

    accunt.addEventListener("focus",function(){
        accunterr.style.display = "none"
        checkerr.style.display = "none"
    },false)
    accunt.addEventListener("blur",function(){
        var inputStr = this.value
        /*
        if (inputStr.length != 8) {
        */
        if (inputStr.length < 6 || inputStr.length >12){
            accunterr.style.display = "block"
            return
        }

        $.post("/checkuserid/",{"userid":inputStr},function(data){
            if(data.status == "error"){
                checkerr.style.display = "block"
            }
        })
        },false)


        /*
        else{
//          验证账号是否被注册
            console.log("*****************1")
            $.ajax({
                url:"/checkuserid/",
                type:"post",
                typedata:"json",
                data:{"checkid":accunt.value},
                success:function(data){
                    console.log(data)
                    if (data.status == "error"){
                        checkerr.style.display = "block"
                    }
                }
            })
        }
    },false)
    */

    pass.addEventListener("focus",function(){
        passerr.style.display = "none"
    },false)
    pass.addEventListener("blur",function(){
        var inputStr = this.value
        if (inputStr.length < 6 || inputStr.length > 16) {
            passerr.style.display = "block"
        }
    },false)


    passwd.addEventListener("focus",function(){
        passwderr.style.display = "none"
    },false)
    passwd.addEventListener("blur",function(){
        var inputStr = this.value
        if (inputStr != pass.value) {
            passwderr.style.display = "block"
        }
    },false)


})