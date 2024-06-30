function loadData(itemData , categoryData){
    items = JSON.parse(itemData)
    categories = JSON.parse(categoryData)
}

function addRow(){
        let newRow = '<td class="py-2 px-4 border-b border-gray-200"  title="Description"> <textarea  name="Description" class = "w-full h-24 bg-white border border-gray-300 rounded py-1 px-2 resize-none"  id="xpanse-description"></textarea></td><td class="py-2 px-4 border-b border-gray-200" ><input  class = "input" name="item" id="item">'
    // Adding the <td> of items
    // --------We will need to add manually items but we'll need to save them into the database
    // Adding the <td> of categories
        newRow+= '</input></td><td class="py-2 px-4 border-b border-gray-200" ><select name="category" id="category">'
    for(i=0 ; i<categories.length ; i++){
        newRow += `<option value=" ${categories[i]}  ">` +categories[i]+'</option>'
        } 
    
    newRow += '</select></td><td class="py-2 px-4 border-b border-gray-200" ><input type="date" name="" id=""></td>'
    
    const tbody = document.querySelector(".exp-table tbody")//when I did it using the id of the table it didn't stay working for too long!!
    // const tbody = document.querySelector('#expansesTable tbody')
    let tr = document.createElement('tr')
    tr.className = 'hover:bg-gray-100'
    tr.innerHTML = newRow
    tbody.appendChild(tr)
    // $(".exp-table tbody").append(newRow)   !!!!!!!!!------This has a weird behaviour-------!!!!!!!!!!!
}
function selectRow(){

}


function deleteRow(){
    /** This is the simplest form of a delete() function , but it lacks precision=>{which row to delete!} */
    let row = document.querySelector('tbody').lastChild
    row.remove()
}

