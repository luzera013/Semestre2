import React, {useState} from 'react'

const Contato = () => {
    const [nome, setNome] = useState('');
    const [email, setEmail] = useState('');
    const [mensagem, setMensagem] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Obrigado, ${nome}! Mensagem enviada`)
        setNome('');
        setEmail('');
        setMensagem('');
    };

  return (
    <div className='p-8 max-w-md mx-auto '>
        <h1 className='text-4xl font-bold text-purple-600 mb-6'>
            Contato
        </h1>

        <form onSubmit={handleSubmit}
        className='space-y-4'>
            <div>
                <label className='block text-gray-700 font-semibold mb-2'>
                    Nome:
                </label>
                <input type="text"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                placeholder='Seu nome'
                required
                className='w-full p-3 border border-gray-300 rounded-lg focus:outline-nome focus:ring focus:ring-purple-500'/>
            </div>
            <div>
                <label className='block text-gray-700 font-semibold mb-2'>
                    Email:
                </label>
                <input type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder='Seu @ Email.com'
                required
                className='w-full p-3 border border-gray-300 rounded-lg focus:outline-nome focus:ring focus:ring-purple-500'/>
            </div>
            <div>
                <label className='block text-gray-700 font-semibold mb-2'>
                    Mensagem:
                </label>
                <textarea
                value={mensagem}
                onChange={(e) => setMensagem(e.target.value)}
                placeholder='Sua Mensagem...:'
                required
                className='w-full p-3 border border-gray-300 rounded-lg focus:outline-nome focus:ring focus:ring-purple-500'/>
            </div>
            <button type='submit'
            className='w-full bg-purple-600 text-white py-3 px-4 rounded-lg hover:bg-purple-700 transition-colors font-semibold'>
                Enviar mensagem
            </button>
        </form>

    </div>
  )
}

export default Contato
