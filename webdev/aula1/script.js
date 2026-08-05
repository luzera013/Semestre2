// Extensão utilizada Quokka

const filmes = ["Familia sacana", "50 tons de cinza", "2 girls one cup"]

console.log(filmes[1])

const filmesModificado = filmes.map((filmeAtual, posicao) => `O filme ${filmeAtual} está na posição ${posicao}`)

console.log(filmesModificado)
console.log(filmes)

const modificarFilmes = (listaFilmes) => listaFilmes.map(filmeAtual => filmeAtual.toUpperCase())
console.log(modificarFilmes(filmes))

// Exercício

const precos = [29.9, 150, 45.5, 8, 320, 99.99]

const precosComDesconto = precos.map((precoAtual) => precoAtual * 0.9)
console.log(precosComDesconto)

const aplicarDesconto = (listaPrecos) => listaPrecos.map(precoAtual => precoAtual * 0.9)
console.log(aplicarDesconto)


// outros

const filme3 = [{
    titulo: "miranha",
    anolacamento: 2026,
    diretor: "lula",
    atores: ["Zendaya", "tom"]
},
{ titulo: "Avengers",
    titulo: "miranha",
    anolacamento: 2026,
    diretor: "lula",
    atores: ["chris", "homem de ferro"]
}]

const criarCard = listaFilmes => listaFilmes.map(filmeAtual2 => {
    return `<div>
                <h1> ${filmeAtual2.titulo}</h1>
                <h3> ${filmeAtual2.anolacamento}</h3>
            </div>`
})