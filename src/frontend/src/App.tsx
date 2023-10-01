import { useEffect, useRef, useState } from 'react';
import './App.css';
import { Action } from './proto/messages';


function App() {
  const [open, setOpen] = useState<boolean>(false);

  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:3000/viewport`);
    ws.binaryType = 'arraybuffer';

    ws.addEventListener('open', () => {
      setOpen(true);
    })

    ws.addEventListener('close', () => {
      setOpen(false);
    })

    ws.addEventListener('error', error => {
      console.error(error)
    })

    ws.addEventListener('message', async msg => {
      const protoMsg = Action.deserializeBinary(new Uint8Array(msg.data));

      switch (protoMsg.type) {
        case (Action.Type.INIT_CANVAS):
          console.log('init canvas');
          break;
        case (Action.Type.SET_PIXELS):
          console.log('set pixels');
          break;
        default:
          console.log('unknown action', protoMsg);
      }

      // setData(msg.data);

      // const data = msg.data as Blob;
      // const buffer = new Uint8ClampedArray(await data.arrayBuffer());
      // const imageData = new ImageData(buffer, 100, 100);

      // const ctx = ref.current?.getContext('2d');
      // if (!ctx) return;

      // ctx.putImageData(imageData, 0, 0);
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
