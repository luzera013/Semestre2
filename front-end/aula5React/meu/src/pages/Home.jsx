import React from 'react'

const Home = () => {
  return (
    <div className='text-center p-8 '>
      <h1 className='text-4xl font-bold text-blue-600 mb-4'>
        Pagina Inicial
      </h1>
      <p className='text-lg text-gray-600'>
        Bem-vindo ao meu app com React-router
      </p>
      <div className='mt-8 p-6 bg-blue-50 rounded-lg'>
          <h2 className='text-xl font-semibold mb-2'>O que você encontra aqui:</h2>  
          <ul className='text-left space-y-2'></ul>
            <li>😊 Navegação simples</li>
            <li>😊 Múltiplas páginas</li>
            <li>😊 React Router</li>
      </div>
    </div>
  )
}

export default Home
