document.addEventListener('DOMContentLoaded',function() {
    let heart = document.querySelector("path");
    document.querySelector('#generate').addEventListener('click', () => food());
    document.querySelector('#favorites').addEventListener('click', () => favorite());
    food();


});

function food() {
    document.querySelector("#generateView").style.display = 'flex';
    document.querySelector("#favoriteView").style.display = 'none';
    document.querySelector('#generateView').innerHTML = '';
    generate_food();
}

function generate_food(){
    fetch(`/food/generate`)
    .then(response => response.json())
    .then(data =>{
        load_food(data);
    })
    .catch(err => {
        console.log(err);
    });
}

function load_food(data) {
    fetch(`https://api.spoonacular.com/recipes/findByNutrients?apiKey=51f720299e1c49f8bb7cb633e7302c5a&minCalories=${data.min}&maxCalories=${data.max}&number=3&random=true`)
    .then(response => response.json())
    .then(meals => {
        meals.forEach(meal => {
            const element1 = document.createElement('div');
            element1.classList.add("meal");
            const title = document.createElement('div');
            title.classList.add("title");
            title.innerHTML=`${meal.title}`
            const picture = document.createElement('img');
            picture.setAttribute('src', `${meal.image}`);
            picture.setAttribute('alt', 'na');
            picture.classList.add("pic");

            const svgDiv = document.createElement('div');    
            let svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
            svg.setAttribute('class','_8-yf5');
            svg.setAttribute('aria-label', 'Like');
            svg.setAttribute('height', '24');
            svg.setAttribute("viewBox", '0 0 48 48');
            svg.setAttribute('width', '24');
            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        
            fetch(`/favoriteStatus/${meal.id}`)
            .then(response => response.json())
            .then(favorite => {
                console.log(favorite);
                if (favorite.status) {
                    svg.setAttribute('fill', '#ed4956');
                    path.setAttribute('d', 'M34.6 3.1c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5s1.1-.2 1.6-.5c1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z');
                }
                else {
                    svg.setAttribute('fill', '#262626');
                    path.setAttribute('d', 'M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z');
                }
            })
            .catch(error => {
                console.log('Error:', error);
            });

            svg.append(path);
            svgDiv.append(svg);
            element1.append(title);
            element1.append(picture);
            element1.append(svgDiv);

            svg.onclick = function() {
                if (svg.getAttribute("fill")=="#ed4956") {
                    svg.setAttribute("fill", "#262626");
                    path.setAttribute("d", "M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z")
                    fetch(`/favoriteStatus/${meal.id}`, {
                        method: 'DELETE',
                        body: JSON.stringify({
                           food_id: meal.food_id 
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                      console.log(data);
                    })
                    .catch(error => {
                    console.log('Error:', error);
                    });
                }
                else {
                    svg.setAttribute("fill", "#ed4956");
                    path.setAttribute("d", "M34.6 3.1c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5s1.1-.2 1.6-.5c1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z")
                    fetch(`/favoriteStatus/${meal.id}`, {
                        method: 'POST',
                        body: JSON.stringify({
                            'calories': meal.calories,
                            'carbs': meal.carbs,
                            'fat': meal.fat,
                            'food_id': meal.food_id,
                            'image': meal.image,
                            'protein': meal.protein,
                            'title': meal.title
                        }) 
                    })
                    .then(response => response.json())
                    .then(data => {
                      console.log('Success:', data);
                    })
                    .catch(error => {
                    console.log('Error:', error);
                    });              
                }
            };

            document.querySelector('#generateView').append(element1);
        });
        console.log(meals)
    })
    .catch(err => {
        console.log(err);
    });
}

function favorite() {
    document.querySelector("#generateView").style.display = 'none';
    document.querySelector("#favoriteView").style.display = 'block';
}