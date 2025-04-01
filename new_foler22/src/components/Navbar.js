import React from 'react'
import { Sheet } from './Slider';
import { PanelLeftOpen} from "lucide-react";
import { useState } from 'react';
function Navbar() {
     const [isOpen, setIsOpen] = useState(false);
  return (
    <div className='text-white flex justify-between'>
        <div className='flex items-center gap-3 p-4 '>
            <PanelLeftOpen className='text-white cursor-pointer' size={30} onClick={()=>{
              setIsOpen(true)
            }}/>
            <div className='font-bold text-lg '>CADGPT</div>
            <Sheet isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <h2 className="text-xl font-semibold">Chat History</h2>
        <p className="mt-2 text-gray-600">This is the sheet content.</p>
      </Sheet>
        </div>
        <div className='flex items-center '>
        <button className="bg-white text-black px-6 py-2 border border-black rounded-full hover:bg-[#414040] hover:border hover:border-white hover:text-white transition mr-5 ">
  Login
</button>
</div>

    </div>
  )
}

export default Navbar