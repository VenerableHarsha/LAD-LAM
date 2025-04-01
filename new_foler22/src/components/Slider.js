import { useState } from "react";
import { X } from "lucide-react";



export const Sheet = ({ isOpen, onClose, children }) => {
  return (
    <div
      className={`fixed inset-0 bg bg-black bg-opacity-50 transition-opacity ${
        isOpen ? "opacity-100 visible" : "opacity-0 invisible"
      }`}
      onClick={onClose} // Close when clicking outside
    >
      {/* Sheet Content - Now Appears from the Left */}
      <div
        className={`fixed top-0 left-0 h-full w-72 bg-black z-4 shadow-lg transform transition-transform ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
        onClick={(e) => e.stopPropagation()} // Prevent closing when clicking inside
      >
        {/* Close Button */}
        <button
          className="absolute top-4 right-4 p-2 rounded-full text-black bg-gray-200 hover:bg-gray-300"
          onClick={onClose}
        >
          <X />
        </button>

        {/* Sheet Content */}
        <div className="p-6">{children}</div>
      </div>
    </div>
  );
};



export default function Slider() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="h-screen flex items-center justify-center bg-gray-100">
      {/* Open Sheet Button */}
      <button
        onClick={() => setIsOpen(true)}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
      >
        Open Sheet
      </button>

      {/* Sheet Component */}
      <Sheet isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <h2 className="text-xl font-semibold text-black">Chat History</h2>
        <p className="mt-2 text-gray-600">This is the sheet content.</p>
      </Sheet>
    </div>
  );
}
