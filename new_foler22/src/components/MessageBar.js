import React from 'react'

function MessageBar({sentence}) {
  return (
    <div className='text-white bg-[#414040]  p-3 px-6 rounded-2xl'>
      {sentence}
    </div>
  )
}

export default MessageBar
