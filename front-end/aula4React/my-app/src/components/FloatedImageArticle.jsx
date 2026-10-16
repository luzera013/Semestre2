import React from 'react'


const FloatedImageArticle = () => {
  return (
    <article className='max-w-3xl mx-auto p-6'>
      <img 
      src="https://picsum.photos/1200" 
      alt="Imagem aleatoria" 
      className='float-left md:float-start mr-4 mb-4 w-full md:w-1/3 rounded-lg shadow-md' />
      <p className='text-gray-700 leading-relaxed text-lg'>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorum iusto ex dicta magnam nam placeat provident, veritatis corrupti corporis quibusdam dolor eveniet ratione? Praesentium non, ipsam quibusdam eligendi accusamus commodi.
      </p>
      <div className='clear-left md:clear-start mt-4 p-2 bg-gray-200 rounded-lg'>
            Este bloco usa <code>clear-left</code> para limpar o float acima -
            em telas menores ou maiores, experimente trocar para <code>md:clear-none</code>
            ou <code>clear-both</code> para ver o comportamento.
      </div>
    </article>
  )
}

export default FloatedImageArticle
