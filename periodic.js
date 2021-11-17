

function populate_class_filter() {
    var classification_xhttp;
    classification_xhttp=new XMLHttpRequest();
    classification_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            dd = document.getElementById("classification");
            for(const classification of response.classifications.all) {
                  var el = document.createElement("option");
                  el.textContent = classification;
                  el.value = classification;
                  dd.appendChild(el);
            }
            populate_state_filter();
        }
     };
    classification_xhttp.open("GET", "http://localhost:5000/periodictable/classifications/", true);
    classification_xhttp.send();

    }
function populate_state_filter(){
    var state_xhttp;
    state_xhttp = new XMLHttpRequest();
    state_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            dd = document.getElementById("state");
            for(const state of response.states.all) {
                  var el = document.createElement("option");
                  el.textContent = state;
                  el.value = state;
                  dd.appendChild(el);
            }
            populate_block_filter();
        }
     };
    state_xhttp.open("GET", "http://localhost:5000/periodictable/standard_states/", true);
    state_xhttp.send();
}

function populate_block_filter(){
    var block_xhttp;
    block_xhttp = new XMLHttpRequest();
    block_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            dd = document.getElementById("block");
            for(const block of response.blocks.all) {
                  var el = document.createElement("option");
                  el.textContent = block;
                  el.value = block;
                  dd.appendChild(el);
            }
            populate_group_filter();
        }
     };
    block_xhttp.open("GET", "http://localhost:5000/periodictable/blocks/", true);
    block_xhttp.send();
}


function populate_group_filter(){
    var group_xhttp;
    group_xhttp = new XMLHttpRequest();
    group_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            dd = document.getElementById("group");
            for(const group of response.groups.all) {
                  var el = document.createElement("option");
                  el.textContent = group;
                  el.value = group;
                  dd.appendChild(el);
            }
            populate_period_filter();
        }
     };
    group_xhttp.open("GET", "http://localhost:5000/periodictable/groups/", true);
    group_xhttp.send();
}

function populate_period_filter(){
    var period_xhttp;
    period_xhttp = new XMLHttpRequest();
    period_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            dd = document.getElementById("period");
            for(const period of response.periods.all) {
                  var el = document.createElement("option");
                  el.textContent = period;
                  el.value = period;
                  dd.appendChild(el);
            }
        }
     };
    period_xhttp.open("GET", "http://localhost:5000/periodictable/periods/", true);
    period_xhttp.send();
}

populate_class_filter();

function displayData() {
    var query_xhttp;
    query_xhttp=new XMLHttpRequest();
    post_data = {
        "classification": document.getElementById("classification").value,
        "standardState": document.getElementById("state").value,
        "block": document.getElementById("block").value,
        "group": document.getElementById("group").value,
        "period": document.getElementById("period").value,
    }
    query_xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            final_calculation(response.elements.all);
        }
     };
    query_xhttp.open("POST", "http://localhost:5000/periodictable/element/fetch", true);
    query_xhttp.setRequestHeader("Content-type", "application/json");
    query_xhttp.send(JSON.stringify(post_data));
}

function final_calculation(final_display) {

    if(final_display.length > 0)
    {
        for(var ans of final_display){
            if(document.getElementById(ans)){
            //    document.getElementById(ans).style.backgroundColor = "#cccccc";
                var element =  document.getElementById(`${ans}`);
                element.style.border = "5px solid red";
                element.classList.remove("hidden");
            }
        }
    } else {
        alert("No element found that matches all the applied filters! Please try again with different filters.");
        location.reload();
    }

}

function displayElement(lnk) {
    var elem = lnk.text;
    var response;
    const Http = new XMLHttpRequest();
    const url = 'http://localhost:5000/periodictable/element/' + elem;
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        response = JSON.parse(Http.responseText);
        var displayDataHTML = "";
        displayDataHTML += `<h1>Detailed Information Of The Selected Element</h1>`;
         displayDataHTML += `<table style = "text-align: center; border: 1px solid black;" cellpadding="7">`;
         displayDataHTML += `<tr><th colspan="2" style="border: 1px solid black; text-decoration: underline;
                                background-color:gray;"> Element: '${elem}'</th></tr>`;

        for (const tab in response) {
           var tableObj = response[tab];
            displayDataHTML += `<tr><td style="border: 1px solid black;">${tab}</td>`
            displayDataHTML += `<td style="border: 1px solid black;">${tableObj}</td></tr>`
        }

        displayDataHTML += "</table><br><br>";
        var divObject = document.getElementById("element_info");
        divObject.innerHTML = displayDataHTML;
        return false;
    }
}