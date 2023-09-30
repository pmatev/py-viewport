export type INIT_CANVAS = {
    width: number;
    height: number;
    background: string;
    render_mode: 'FRAMEBUFFER' | '2D' | '3D';
}

export type SET_PIXELS = {
    width: number;
    height: number;
    data: Blob;
}

export type ADD_IMAGE_LAYER = {
    width: number;
    height: number;
    data: Blob;
    name: string;
}

type ALL_ACTIONS = 'INIT_CANVAS'
    | 'SET_PIXELS'
    | 'ADD_IMAGE_LAYER'
;

type ALL_ACTIONS_PAYLOADS = INIT_CANVAS
    | SET_PIXELS
    | ADD_IMAGE_LAYER
;

export type Action = {
    type: ALL_ACTIONS,
    payload: ALL_ACTIONS_PAYLOADS
}