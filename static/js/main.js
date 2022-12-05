function capitalize(s)
{
    return s[0].toUpperCase() + s.slice(1);
}
function viewDrugInfo(drugInfo) {
    var rowElemt = document.getElementById("result_row")
    rowElemt.innerHTML = ""
    headerResult = document.createElement("h3")
    headerResult.innerText = "Result"
    rowElemt.appendChild(headerResult)
    if (drugInfo["drugName"] === "Not found"){
        reElemt = document.createElement("span")
        reElemt.innerHTML = "Not Found: " + drugInfo["searchName"]
        rowElemt.appendChild(reElemt)

    }
    else{
        tableElemt = document.createElement("table")
        tableElemt.setAttribute("class", "table")
        theader = document.createElement("thead")
        theader.innerHTML = "<tr>\n" +
            "                <th scope=\"col\">#</th>\n" +
            "                <th scope=\"col\"></th>\n" +
            "              </tr>"
        tableElemt.appendChild(theader)
        tbody = document.createElement("tbody")
        keys = ["drugName", "inchiKey", "drugBankID", "smile", "synNames" , ]

        for (const key of keys){
            data = drugInfo[key]
            if (key==="synNames"){
                data = data.join(', ')
            }
            trow = document.createElement("tr")
            trow.innerHTML = "<th scope=\"row\">" + capitalize(key)+ "</th>" + "\n"
                            + "<td>" + data + "</td>"
            tbody.appendChild(trow)
        }

        tableElemt.appendChild(tbody)
        rowElemt.appendChild(tableElemt)
    }
}


