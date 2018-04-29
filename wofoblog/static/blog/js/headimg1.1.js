


      $("#avatarSlect").change(function () {
          var obj=$("#avatarSlect")[0].files[0];
          var fr=new FileReader();
           fr.onload=function () {
               $("#avatarPreview").attr('src',this.result);
               $("#avatar").attr('src',this.result);

               $("#avatar").val(this.result);
      };
      fr.readAsDataURL(obj);
    })



    function bindAvatar1() {
    var csrf = $("input[name='csrfmiddlewaretoken']").val();
    var formData=new FormData();
    formData.append("csrfmiddlewaretoken",csrf);
    formData.append("name",$('#name').val());
    formData.append("pwd",$('#pwd').val());
    formData.append("email",$('#email').val());
    formData.append("phone",$('#phone').val());
    formData.append("common",$('#common').val());
    formData.append('avatar', $("#avatarSlect")[0].files[0]);  /*获取上传的图片对象*/

    $.ajax({
      url: '/blog/imageupdate/',
      type: 'POST',
      data: formData,
      contentType: false,
      processData: false,
      success: function (args) {
                /*console.log(args);  服务器端的图片地址*/

              $("#avatar").val('/'+args);  /*将服务端的图片url赋值给form表单的隐藏input标签*/
              alert("修改成功")
     }
      })
  }