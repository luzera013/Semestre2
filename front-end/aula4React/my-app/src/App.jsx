import React from 'react'
import ThreeColumnHero from './components/ThreeColumnHero'
import DecoratedText from './components/DecoratedText'
import FloatedImageArticle from './components/FloatedImageArticle'

const App = () => {
  return (
    <div className='space-y-12'>
      <ThreeColumnHero></ThreeColumnHero>
      <DecoratedText></DecoratedText>
      <FloatedImageArticle></FloatedImageArticle>
    </div>
  )
}

export default App
