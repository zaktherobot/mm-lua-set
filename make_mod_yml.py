import sys,io,zipfile,os,yaml


def make_script_mod(script_name):
    return {"title":script_name,
                    "description": "See the lua for details",
                    "assets" : [{"name":"scripts/"+script_name,"method":"copy","source":[{"name":script_name}]}]}
def make_mod_yml():
    script_file = sys.argv[1]
    if script_file.endswith('.lua'):
        localfile = os.path.basename(script_file)
        script_name_zip = localfile.removesuffix(".lua") + ".zip"
        data = io.BytesIO()
        loaded_script = None
        with open(script_file, 'r') as fin:
            loaded_script = fin.read()
        data = io.BytesIO()
        with zipfile.ZipFile(data,"w") as outZip:
            outZip.writestr(localfile,loaded_script)
            outZip.writestr("mod.yml", yaml.dump(make_script_mod(localfile), line_break="\r\n"))
            outZip.close()
        data.seek(0)
        with open(script_name_zip, "wb") as out_zip:
            out_zip.write(data.getbuffer())


if __name__ == "__main__":
    make_mod_yml()