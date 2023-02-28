var http = require('http');
var fs = require('fs')
var url = require('url');

/*
second attempt to deal with non-ascii characters

function query_string_to_ascii(query_string) {
    // Decodifica a string percent-encoded
    let decoded_string = decodeURIComponent(query_string);
    // Converte para uma string normal em ascii
    let ascii_string = new TextDecoder('iso-8859-1').decode(
      new TextEncoder().encode(decoded_string)
    );
    return ascii_string;
  }
*/

http.createServer(function  (req, res) {
    var pedido = url.parse(req.url,true).pathname.substring(1); 
    console.log(pedido)
    var d = new Date().toISOString().substring(0,16)
    console.log(req.method + " " + req.url + " " + d);
    console.log(pedido)
    pedido = decodeURIComponent(pedido)
    console.log(pedido)
    if (!pedido){
        pedido = 'index'
    }
    fs.readFile(pedido+'.html', function (err,data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        if(err){
            res.write('Erro na leitura do ficheiro ' + err)
        }
        else{
            res.write(data)
        }
        
        res.end();

    })
    
}).listen(7788)

console.log('Server listening on 7788')