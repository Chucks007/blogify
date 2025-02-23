// Defining Toasts
var successAlert = document.getElementById('success-toast');
var successText = document.getElementById("success-span");

var warningAlert = document.getElementById('warning-toast');
var warningText = document.getElementById("warning-span");

$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

$("#chtHead").click(function() {
  // Toggle chatbar sliding in/out
  var elementClasses = document.getElementById("chatbar");
  var classesArr = elementClasses.classList;

  if(classesArr.value.includes("slideout")) {  
    elementClasses.classList.remove("slideout");
    elementClasses.classList.add('slidein');
  } else if (classesArr.value.includes("slidein")) {  
    elementClasses.classList.remove("slidein");
    elementClasses.classList.add('slideout');
  } else {
    elementClasses.classList.add('slideout');
  }
});

// show and hide password while changing the icon function
function togglePassword(){
    $("body").on('click', '.toggle', function() {
        $(this).toggleClass("bi bi-eye");
        var input = $("#password");
        if (input.attr("type") === "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });
}

// show and hide confirm password
function toggleConfirmPassword(){
  $("body").on('click', '.toggle', function() {
      $(this).toggleClass("bi bi-eye");
      var input = $("#confirmPassword");
      if (input.attr("type") === "password") {
        input.attr("type", "text");
      } else {
        input.attr("type", "password");
      }
    });
}

function scrollTillBottom(){
  var scrollEnd = document.getElementById('innerContentBox');
  scrollEnd.scrollTop = scrollEnd.scrollHeight;
}

function logIn(){
  // Read username and password values.
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  // Removed reCAPTCHA: no longer retrieving g-recaptcha-response.
  var csrf = document.getElementById('csrf').value;

  if (username === "" || username.length < 5) {
    var text = "Please enter a valid username!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  }
  if (password === "") {
    var text = "Please enter a valid password!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  } else {
    var data = {
      'username': username,
      'password': password
      // Removed gReCaptcha property.
    };

    fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf,
      },
      body: JSON.stringify(data)
    })
    .then(result => result.json())
    .then(response => {
      if (response.status == 200) {
        window.location.href = '/';
      } else {
        warningText.innerHTML = response.message;
        var bsAlert = new bootstrap.Toast(warningAlert);
        bsAlert.show();
      }
    });
  }
}

function signUp(){
  var firstname = document.getElementById('firstname').value;
  var lastname = document.getElementById('lastname').value;
  var email = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  var confirmpassword = document.getElementById('confirmPassword').value;
  // Removed reCAPTCHA reference.
  var csrf = document.getElementById('csrf').value;

  if (firstname === "" || lastname === "" || firstname.length < 2 || lastname.length < 2) {
    var text = "Please enter a valid firstname or lastname!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  }
  if (email === "" || email.indexOf("@") === -1 || email.length < 6) {
    var text = "Please enter a valid email address!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  }
  if (password === "" || password.length < 8) {
    var text = "Password should be at least 8 characters long!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  }
  if (password !== confirmpassword) {
    var text = "Confirm password does not match!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  } else {
    var data = {
      'firstname': firstname,
      'lastname': lastname,
      'username': email,
      'password': password,
      'email': email
      // Removed gReCaptcha property.
    };

    fetch('/api/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf,
      },
      body: JSON.stringify(data)
    })
    .then(result => result.json())
    .then(response => {
      if (response.status == 200) {
        $("#signup-container").load(window.location.href + " #signup-container");
        successText.innerHTML = response.message;
        var toastDiv = document.getElementById('success-toast-with-img');
        var bsAlert = new bootstrap.Toast(toastDiv);
        bsAlert.show();
      } else {
        warningText.innerHTML = response.message;
        var bsAlert = new bootstrap.Toast(warningAlert);
        bsAlert.show();
      }
    });
  }
}

function blogComment(event){
  event.preventDefault();
  var postComment = document.getElementById('postComment').value;
  var postId = document.getElementById('postId').value;
  var csrf = document.getElementById('csrf').value;

  if (postComment === ''){
    var text = "Please enter a message!";
    warningText.innerHTML = text;
    var bsAlert = new bootstrap.Toast(warningAlert);
    bsAlert.show();
    return false;
  } else {
    var data = {
      'postComment': postComment,
      'postId': postId
    };

    fetch('/api/comment/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf,
      },
      body: JSON.stringify(data)
    })
    .then(result => result.json())
    .then(response => {
      if (response.status == 200) {
        $("#innerContentBox").load(window.location.href + " #innerContentBox");
        // Clear the comment input field.
        document.querySelector('input[name="postComment"]').value = '';
      } else {
        warningText.innerHTML = response.message;
        var bsAlert = new bootstrap.Toast(warningAlert);
        bsAlert.show();
      }
    });
  }
}

function deleteComment(event){
  event.preventDefault();
  var cmd = document.getElementById('userCommentID').value;
  var csrf = document.getElementById('csrf').value;
  $("#innerContentBox").load(window.location.href + " #innerContentBox");
}

function blogContact(){
    var name  = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var desc = document.getElementById('desc').value;
    // Removed reCAPTCHA reference.
    var csrf = document.getElementById('csrf').value;

    var text;
  
    if (name === "" || name.length < 5) {
      text = "Please enter a valid name!";
      warningText.innerHTML = text;
      var bsAlert = new bootstrap.Toast(warningAlert);
      bsAlert.show();
      return false;
    }
  
    if (email === "" || email.indexOf("@") === -1 || email.length < 6) {
      text = "Please enter a valid email address!";
      warningText.innerHTML = text;
      var bsAlert = new bootstrap.Toast(warningAlert);
      bsAlert.show();
      return false;
    }
  
    if (desc === "" || desc.length <= 10) {
      text = "Some more information would be better!";
      warningText.innerHTML = text;
      var bsAlert = new bootstrap.Toast(warningAlert);
      bsAlert.show();
      return false;
    } else {
      $.ajax({
        type: 'POST',
        url: '',
        data: {
          name: name,
          email: email,
          desc: desc
          // Removed gReCaptcha from data.
        },
        headers: {
          'X-CSRFToken': csrf,
        },
        success: function(data){
          document.getElementById("contact-form").reset(); 
        }
      });
    }
}

$('ul.checklist-select li').click(function() {
      var selectID = $(this).attr('id');
      $('ul.checklist-select li').removeClass('active');
      $(this).addClass('active');

      $('div.tabcontent').removeClass('selected');
      $('div.tabcontent').addClass('box');
      $('.' + selectID + '-tabcontent').removeClass('box');
      $('.' + selectID + '-tabcontent').addClass('selected');
});  
 
$('div.blogHead').click(function() {
  var blogID = $(this).attr('id');
  $('.comment-' + blogID).toggleClass('disBlock');
});  

function toggleConfirmation(){
  $('.confirmation').addClass('toggle-confirmation');
}

$('#btn-confirmation-close').click(function() {
  $('.confirmation').removeClass('toggle-confirmation');
});

function deleteProPic(){
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to DELETE your Profile Picture?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
    $.ajax({
      url: "/deleteProPic/",
      success: function(json) {
        $('.confirmation').removeClass('toggle-confirmation');
        $("#profilePageRow").load(" #profilePageRow");
        $("#navbar").load(" #navbar");
        successText.innerHTML = 'Profile Picture Deleted Successfully!';
        var bsAlert = new bootstrap.Toast(successAlert);
        bsAlert.show();
      }
    });
  });
}

function delBlog(blog_id){
  var id = blog_id.split('-')[1];
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to DELETE this blog?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
    $.ajax({
      url: "/blogDelete/" + id,
      success: function(json) {
        $('.confirmation').removeClass('toggle-confirmation');
        $(".myBlogsList").load(" .myBlogsList");
      }
    });
  });
}

function cookieAcceptance(){
  $.ajax({
    url: "/cookieAcceptance/",
    success: function(json) {
      $("#cookieBox").load(" #cookieBox");
    }
  });
}

function disableUser(user_id){
  var id = user_id.split('-')[1];
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to DISABLE this user?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
   $.ajax({
      url: "/adminView/disableUser/" + id,
      success: function(json) {
        $("#usersTable").load(window.location.href + " #usersTable");
        $("#navbar").load(" #navbar");
        successText.innerHTML = 'User Disabled Successfully!';
        var bsAlert = new bootstrap.Toast(successAlert);
        bsAlert.show();
      }
   });
  });
}

function deleteUser(user_id){
  var id = user_id.split('-')[1];
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to DELETE this user?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
    $.ajax({
      url: "/adminView/deleteUser/" + id,
      success: function(json) {
        $("#usersTable").load(window.location.href + " #usersTable");
        successText.innerHTML = 'User Deleted Successfully!';
        var bsAlert = new bootstrap.Toast(successAlert);
        bsAlert.show();
      }
    });
  });
}

function activateUser(user_id){
  var id = user_id.split('-')[1];
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to ACTIVATE this user?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
    $.ajax({
      url: "/adminView/activateUser/" + id,
      success: function(json) {
        $("#usersTable").load(window.location.href + " #usersTable");
        successText.innerHTML = 'User Activated Successfully!';
        var bsAlert = new bootstrap.Toast(successAlert);
        bsAlert.show();
      }
    });
  });
}

function resendVerification(user_id){
  var id = user_id.split('-')[1];
  var confirmation = document.getElementById('confirmationMessage');
  confirmation.innerHTML = 'Are you sure you want to resend the verification email to this user?';
  toggleConfirmation();
  $("#userConfirmed").on('click', function(){
    $.ajax({
      url: "/adminView/resendVerification/" + id,
      success: function(json) {
        $("#usersTable").load(window.location.href + " #usersTable");
        successText.innerHTML = 'Email Sent Successfully!';
        var bsAlert = new bootstrap.Toast(successAlert);
        bsAlert.show();
      }
    });
  });
}

function closeConfirmationBox(){
  $('.confirmation').removeClass('toggle-confirmation');
}
