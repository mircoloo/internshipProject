
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    try{
        res.render("/index.php")
    }catch(err){
        console.log(err)
    }
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

