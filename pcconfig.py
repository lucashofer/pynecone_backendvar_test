import pynecone as pc

config = pc.Config(
    app_name="backend_variables",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
