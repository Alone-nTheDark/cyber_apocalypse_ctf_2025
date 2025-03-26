import tensorflow as tf

model = tf.keras.models.load_model(
      'malicious.h5',
      compile=False,
      safe_mode=False
)

model.compile()

import base64
import marshal
import dis

lv = model.get_layer('hyperDense')
config = lv.get_config()

print(config)

fn_code = config['function']['config']['code']

decoded_bytes = base64.b64decode(fn_code)

fn_code_obj = marshal.loads(decoded_bytes)

print("\nDisassembled bytecode:")
dis.dis(fn_code_obj)

output_code = config['output_shape']['config']['code']

decoded_bytes = base64.b64decode(output_code)

coutput_ode_obj = marshal.loads(decoded_bytes)

print("\nDisassembled bytecode:")
dis.dis(coutput_ode_obj)

def extract_flag(code_obj):
    for const in code_obj.co_consts:
        if isinstance(const, tuple) and all(isinstance(x, int) for x in const):
            try:
                return ''.join([chr(x) for x in const])
            except ValueError:
                continue
    return "Flag not found!"

flag = extract_flag(fn_code_obj)
print(flag)