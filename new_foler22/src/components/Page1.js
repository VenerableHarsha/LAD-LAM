import React from 'react'
import Navbar from './Navbar'
import { Typinggg } from '../npm-installs/Typinggg'
import ChatInput from './ChatInput'
import MessageBar from './MessageBar'
import { useSelector } from 'react-redux'

const randomSentences = [
    "The quick brown fox jumps over the lazy dog.",
    "She opened the book and discovered a world of adventure.",
    "Life is what happens when you're busy making other plans.",
    "The stars shimmered in the midnight sky.",
    "Coding is like solving a puzzle with infinite solutions.",
    "He walked into the coffee shop and ordered his usual.",
    "Creativity is intelligence having fun.",
    "The waves crashed against the shore, whispering secrets to the sand.",
    "She found an old letter tucked inside the pages of a dusty book.",
    "A journey of a thousand miles begins with a single step."
  ];
  
  console.log(randomSentences);
  
function Page1() {
  const{first_send_check}=useSelector((state)=>state.messages);
  const { messages } = useSelector((state) => state.messages);
  console.log(messages);
  return (
    <div className="h-screen bg-[#2c2b2b] w-screen md:w-[60%] flex flex-col scrollbar-hide">
        <Navbar/>
        <div className='flex justify-center items-center flex-grow overflow-y-auto text-white text-5xl scrollbar-hide'>
          {!first_send_check&& <Typinggg/>}
        </div>
        <div className='flex flex-col items-end mr-10 gap-2 mb-4 overflow-y-auto max-h-[50vh] p-2 scrollbar-hide'>
          {messages.map((sentence, index) => (
            <MessageBar key={index} sentence={sentence} />
          ))}
        </div>
        <ChatInput/>
    </div>
  )
}

export default Page1