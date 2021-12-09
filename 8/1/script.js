window.onload = function(){
    console.log('Tekst 1');
    window.alert('Tekst 2')
}

document.getElementById('btnClick').onclick = function() {
    let form_input = document.forms[0].elements;
    document.getElementById('output').innerHTML = "<b>Value1 :</b> " + form_input[0].value + "<br><b>Value2 :</b> " + form_input[1].value;
    console.log(typeof(form_input[0].value))
    console.log(typeof(form_input[1].value))

}