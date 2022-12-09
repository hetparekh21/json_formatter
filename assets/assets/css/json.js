function json_format() {
 
    // get the value of the text area
    var json = document.getElementById("data").value;

    // parse json
    var obj = JSON.parse(json);

    // format json
    var pretty = JSON.stringify(obj, undefined, 4);

    // set the value of the text area
    document.getElementById("formatted").value = pretty;

    // print json
    console.log(pretty);
}

function clear_data(){
    document.getElementById("data").value = "";
    
}

function clear_formatted(){
    document.getElementById("formatted").value = "";
}


function example(){

    var json = '{"store":{"book":[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"Evelyn Waugh","title":"Sword of Honour","price":12.99},{"category":"fiction","author":"J. R. R. Tolkien","title":"The Lord of the Rings","isbn":"0-395-19395-8","price":22.99}],"bicycle":{"color":"red","price":19.95}}}';
    // set the value of the text area
    document.getElementById("data").value = json;

}
