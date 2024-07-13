// improtar express
const express = require("express"); //(forma antigua)
const { PrismaClient } = require("@prisma/client");
const homeRouter = require("./routes/homeRouter");

//instanciar express en una variable
const app = express();
const prisma = new PrismaClient();

//vmoas andicar que nuestro proyecto puyede recibir json desde el cliente
app.use(express.json());

app.get ('/books', async function( req, res){
    const books = await prisma.book.findMany();

    return res.json({
        books,
      });
    });

app.get ("/books/:id", async function (req, res){ 
  const bookId = Number(req.params.id); //estamos convirtiendo en numero
  const book = await prisma.book.findUnique({
    where:{
      id: bookId,
    },
  }) ;

  return res.json ({book});
 
});

    app.post("/books", async function (req, res) {
      const book = req.body;
    
      const newBook = await prisma.book.create({
        data: {
          title: book.title,
          author: book.author,
          summary: book.summary,
          isbn: book.isbn,
          is_published: book.is_published,
          published_date: new Date(book.published_date),
        },
      });
    
      return res.json(
        {
          book: newBook,
        },
        201
      );
    });

  app.put("/books/:id", async function (res, res){
    const bookUpdated = await prisma.book.update({
      where: {
        id:Number(req.params.id),
      },
      //es la informacion que vamos a actualizar req.body
      data: req.body,
    });
    return res.json({
      book: bookUpdated,
    });
  });
 
  app.delete("/books/:id", async function (req,res){
    const bookDeleted = await prisma.book.delete({
      where:{
        id:Number(req.params.id),
      },
    });
    return res.json({
      book: bookDeleted,
    });
  })
  

app.listen(9000, function(){
    console.log('El servidor inicio de http://localhost:9000');
})
