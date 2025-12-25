---
id: juce
name: JUCE
category: Audio
level: learning
---

# JUCE

Framework C++ para desarrollo de aplicaciones de audio y plugins.

## Uso actual

- Resonant Graph Synth (primer proyecto)

## Conceptos aprendidos

### Arquitectura de Plugin

```cpp
// AudioProcessor - El cerebro del plugin
class MyProcessor : public juce::AudioProcessor {
    void prepareToPlay(double sampleRate, int samplesPerBlock);
    void processBlock(juce::AudioBuffer<float>&, juce::MidiBuffer&);
};

// AudioProcessorEditor - La interfaz
class MyEditor : public juce::AudioProcessorEditor {
    void paint(juce::Graphics&);
    void resized();
};
```

### Parametros

```cpp
juce::AudioProcessorValueTreeState parameters;

// Slider attachment
std::unique_ptr<SliderAttachment> attachment;
attachment = std::make_unique<SliderAttachment>(params, "gain", slider);
```

### MIDI Keyboard

```cpp
juce::MidiKeyboardState keyboardState;
juce::MidiKeyboardComponent keyboard{keyboardState,
    juce::MidiKeyboardComponent::horizontalKeyboard};
```

## Build con CMake

```cmake
add_subdirectory(JUCE)

juce_add_plugin(MyPlugin
    IS_SYNTH TRUE
    NEEDS_MIDI_INPUT TRUE
    FORMATS Standalone VST3 AU
)

target_link_libraries(MyPlugin
    PRIVATE
        juce::juce_audio_utils
        juce::juce_dsp
)
```

## Targets generados

- Standalone (.app)
- VST3 (.vst3)
- AU (.component)

## Recursos

- [JUCE Tutorials](https://juce.com/learn/tutorials)
- [JUCE API](https://docs.juce.com/master/)
