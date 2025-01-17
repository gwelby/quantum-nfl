uniform float time;
uniform float consciousness;
uniform vec3 teamColor;
varying vec2 vUv;
varying vec3 vNormal;

void main() {
    float wave = sin(vUv.x * 10.0 + time) * 0.5 + 0.5;
    float conscious = smoothstep(0.0, 1.0, consciousness);
    vec3 glowColor = mix(teamColor, vec3(1.0), conscious * wave);
    float fresnel = pow(1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0)), 3.0);
    gl_FragColor = vec4(glowColor * (fresnel + 0.5), 1.0);
}
