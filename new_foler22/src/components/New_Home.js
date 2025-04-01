import React from 'react'
import Page1 from './Page1'
import Page2 from './Page2'
import Slider from './Slider'
function New_Home() {
  return (
    <div className='flex flex-col md:flex-row '>
        <Page1/>
        <Page2/>
      
      
    </div>
  )
}

export default New_Home
