import React from 'react'

const DecoratedText = () => {
  return (
    <div className='p-6 bg-gray-100 flex justify-center'>
        <p className='inline-block bg-gradent-to-r from-indigo-500 to-pink-500
        px-4 py-2 rounded-lg leading-tight text-xl box-decoration-clone shadow-lg
        hover:box-decoration-slice transition-all duration-300'>
            Este é um texte longo que vai quebrar em multiplas linhas em telas menores,
            mostrando o efeito do <span className='font-bold underline'>box-decoration-break</span>
            no Tailwind CSS.
        </p>
    </div>
  )
}

export default DecoratedText
