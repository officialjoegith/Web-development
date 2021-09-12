const app= require('express')()
const cors = require('cors')

const PORT = 8000;

let posts = require('./posts.json')

app.get('/posts/',(req, res) => {
    res.send(JSON.stringify(posts));
    res.end();  
})

app.listen(PORT, () =>{
    console.log(`App is running on port: ${PORT}`)
})