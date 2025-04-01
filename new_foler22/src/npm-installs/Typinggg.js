import React from 'react';
import Typed from 'typed.js';

 export function Typinggg() {
  // Create reference to store the DOM element containing the animation
  const el = React.useRef(null);

  React.useEffect(() => {
    const typed = new Typed(el.current, {
        strings: [
            '<i>Wanna ease your Work.</i> ',
            'Automate your CAD with <br><div class="flex justify-center items-center">CADGPT .</div>'
          ],
      typeSpeed: 50,
    });

    return () => {
      // Destroy Typed instance during cleanup to stop animation
      typed.destroy();
    };
  }, []);

  return (
    <div className="App">
      <span ref={el} />
    </div>
  );
}