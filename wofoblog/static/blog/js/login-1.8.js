/*
 *用于登录页面
*/
 function loginfunction(){
	var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:"/blog/login/",
        type:'POST',
        headers:{'X-CSRFToken': csrf},
        data:$('#login-two').serialize(),
        success:function(data){

               var obj = JSON.parse(data);
                        if(obj.status){

                            window.location.href=obj.error
                        }else{
                            alert(obj.error)
                        }
            },
        error:function(data){
            alert('error')

             var obj = JSON.parse(data);
                        if(obj.status){
                            window.location.href=obj.error
                        }else{
                            alert(obj.error)
                        }
        }

        })
 }
 function returnlogin(){
    $('#login-two')[0].classList.remove('hidden');
    $('#login-one')[0].classList.remove('hidden');
    $('#register-one')[0].classList.add('hidden');
    $('#register-two')[0].classList.add('hidden');
 }

 function createfunction(){

    $('#register-one')[0].classList.remove('hidden');
    $('#register-two')[0].classList.remove('hidden');
    $('#login-one')[0].classList.add('hidden');
    $('#login-two')[0].classList.add('hidden');
    }

 function registerunction(){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url:"/blog/register/",
        type:'POST',
        headers:{'X-CSRFToken': csrf},
        data:$('#register-two').serialize(),
        success:function(data){
             var obj = JSON.parse(data);
                        if(obj.status){
                            alert(obj.error)
                        }else{
                            alert(obj.error)
                        }
            },
        error:function(data){
             alert('error')
             var obj = JSON.parse(data);
                        if(obj.status){
                            alert(obj.error)
                        }else{
                            alert(obj.error)
                        }
        }


   })



 }