function card({Nome, Cargo}) {
    return (
        <div>
            <h1>{Nome}</h1>
            <p>{Cargo}</p>
            <button>Seguir</button>
        </div>
    )
}


//////////////////////////////////

function Card({ Nome, Atributo, Avaliacao }) {
    const estrela = 'x'.repeat(nota) + 'X'.repeat(5 - nota)

    return (
        <div>
            <h1>{Nome}</h1>
            <p>{Atributo}</p>
            <span>{Avaliacao}</span>
        </div>
    );
}

/////////////////////////////////////////////////////

function Card({ Nome, preco, prestacao }) {
    const resultado = prestacao * preco;

    return (
        <div>
            <h1>{Nome}</h1>
            <p>R$ {prestacao * preco}</p>
            <strong>{resultado}</strong>
        </div>
    );
} 

