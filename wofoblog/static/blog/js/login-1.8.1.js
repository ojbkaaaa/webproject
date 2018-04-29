/*
 *用于登录页面
*/

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

$(document).ready(function(){
    $('#infostatus').click();
})