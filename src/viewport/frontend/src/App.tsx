import { useEffect, useRef, useState } from 'react';
import './App.css';


function App() {
  const [open, setOpen] = useState<boolean>(false);
  const [error, setError] = useState<Event | undefined>(undefined);
  const [data, setData] = useState<Blob | undefined>(undefined);

  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:3000/viewport`);

    ws.addEventListener('open', () => {
      setOpen(true);
    })

    ws.addEventListener('close', () => {
      setOpen(false);
    })

    ws.addEventListener('error', error => {
      setError(error);
    })

    ws.addEventListener('message', async msg => {
      setData(msg.data);

      const data = msg.data as Blob;
      const buffer = new Uint8ClampedArray(await data.arrayBuffer());
      const imageData = new ImageData(buffer, 100, 100);

      const ctx = ref.current?.getContext('2d');
      if (!ctx) return;

      ctx.putImageData(imageData, 0, 0);
    });
  }, []);

  return (
    <div>
      Websocket status: {open.toString()}
      <div>
        <canvas width={100} height={100} ref={ref} />
      </div>
    </div>
  )
}

export default App;
