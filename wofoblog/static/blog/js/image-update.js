$(function () {
      bindAvatar3();
 });

 /*window.URL.createObjectURL本地预览*/
 function bindAvatar3() {
   console.log(3);
      $("#avatarSlect").change(function () {
          var obj=$("#avatarSlect")[0].files[0];
          var wuc=window.URL.createObjectURL(obj);
           $("#avatar").attr('src',wuc);
           $("#avatarPreview").attr('src',wuc);
           $("#avatar").val(wuc);

   })

 }