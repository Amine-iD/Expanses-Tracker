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
    tr.classList.add('hover:bg-gray-100','cursor-pointer')
    tr.innerHTML = newRow
    tr.id = 'row'
    tbody.appendChild(tr)
    // $(".exp-table tbody").append(newRow)   !!!!!!!!!------This has a weird behaviour-------!!!!!!!!!!!

    let table = document.querySelector('.exp-table')
    let selected = null ;
    table.addEventListener('click' , function(e){
        if (selected) selected.classList.remove('selected'); // unselect any previously selected row
        if (e.target.matches('textarea , input  , option , select')) 
            return;
        
        let target = e.target.closest('tr')
        if (target){
            selected = target
            selected.classList.add('selected')
        }
    })
    // unselect the row once clicked outside of the table
    document.addEventListener('click' , function(e){
        if (!table.contains(e.target)){
            if (selected){
                selected.classList.remove('selected')
                selected = null;
            }
        }
    })
    

}

function deleteRow(){
   let selectedRow = document.querySelector('.selected')
   if (selectedRow) selectedRow.remove();
}
