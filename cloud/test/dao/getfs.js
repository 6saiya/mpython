let fs = require('fs'),
    path = require('path'),
    out = process.stdout;

let getfs = {
    getfs: (req, res, next) => {
        let date = new Date()
        let name = req.query.title + date.getFullYear() + date.getMonth() + date.getDate() + date.getHours() + date.getMinutes() + date.getSeconds()
        fs.writeFile(path.join(__dirname, `../folder/${req.query.id}/${name}.py`), req.query.msg, 'utf8', function (err) {
            if (err) {
                console.log(err);
            } else {
                console.log("创建成功");
            }
        })

        res.end('test')
       
    }
}

module.exports = getfs;