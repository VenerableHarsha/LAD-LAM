import { useState, useRef, useEffect } from "react";
import { Send } from "lucide-react";
import { useDispatch } from "react-redux";
import { addMessage, setFirstSendCheck } from "./Store/Slices/Messages";

const ChatInput = ({ onSend }) => {
  const [message, setMessage] = useState("");
  const textareaRef = useRef(null);
  const dispatch = useDispatch();

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [message]);

  const handleSend = () => {
    const trimmed = message.trim();
    if (trimmed !== "") {
      dispatch(setFirstSendCheck());
      dispatch(addMessage({ id: Date.now(), role: "user", content: trimmed }));
      if (onSend) onSend(trimmed);
      setMessage("");
    }
  };

  return (
    <div className="flex py-8 gap-2 px-4 p-2 rounded-3xl shadow-md w-[90%] bg-[#494747] justify-center items-center ml-8 mb-7">
      <textarea
        ref={textareaRef}
        className="resize-none flex justify-center items-center overflow-hidden bg-[#494747] w-full p-2 rounded-lg border-none focus:outline-none placeholder-white text-white"
        rows={1}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
          }
        }}
      />
      <button
        onClick={handleSend}
        className="p-2 rounded-full bg-white hover:bg-blue-600 flex items-center justify-center w-10 h-10"
      >
        <Send className="w-5 h-5 text-black" />
      </button>
    </div>
  );
};

export default ChatInput;
