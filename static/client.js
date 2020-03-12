function addInOut(){
  var success;
  var message;

  input = document.getElementById('product').value;

  //formobj = new FormData();
  //formobj.append('product', input);

  //httphelper = new XMLHTTPRequest();
  //myhttphelper.open("POST", "http://localhost:5000/update");
  //myhttphelper.send(formobj);
  errormessage = document.getElementById('errormessage');
  errormessage.innerHTML = "hej detta är christian";

}

function updateLagersaldo(){
  var formObj = {
  product : document.getElementById('product').value,
  city : document.getElementById('city').value,
  amount : document.getElementById('amount').value
  };

  var formData = new FormData();

  formData.append('product, formObj.product');
  formData.append('city, formObj.city');
  formData.append('amount, formObj.amount');
}

function openPage(evt, pageName) {
  var i, pages, tablinks;

  pages = document.getElementsByClassName("pages");
  /*for (i = 0; i < pages.length; i++) {
    pages[i].style.display = "none";
  }
  */
  tablinks = document.getElementsByClassName("tabbuttons")
  for(i = 0; i< pages.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" activetab", "");
  }
  if(localStorage.currentpage != null){
    document.getElementById(localStorage.currentpage).style.display = "block";
  }
  else{
  document.getElementById(pageName).style.display = "block";
  localStorage.currentpage = pageName;
  }
  evt.currentTarget.className += " activetab";
  var str = pageName;
  location.href='/' + str;
}
