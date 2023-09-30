type Viewport = {
  DATA: any;
}

// declare var __VIEWPORT__: Viewport;

declare global {
  interface Window {
    __VIEWPORT__: Viewport;
  }
}


type Action = {
  type: string;
  data: any;
}



const root = document.getElementById('viewport-scene-root');


function run() {
  const actions = window.__VIEWPORT__.DATA as Action[];

  for (const action of actions) {
    switch (action.type) {
      case 'INIT_CANVAS':
        init_canvas(action.data);
        break;
      default:
        console.log('unknown action');
    }
  }
}

function init_canvas(msg: any) {

}

export {}
