export type Point2D = {
    x: number;
    y: number;
}

export type Point3D = {
    x: number;
    y: number;
    z: number;
}

export type Tensor = {
    shape: number[];
    data: Uint32Array;
}