import pynecone as pc


class ParentState(pc.State):
    
    _backend_count: int = 0

    def increment_parent_backend(self):
        self._backend_count += 1

    def print_parent_backend(self):
        return pc.console_log(self._backend_count)

    @pc.var
    def parent_backend(self):
        return self._backend_count


class ChildState(ParentState):

    def increment_child_backend(self):
        self._backend_count += 1

    @pc.var
    def child_backend(self):
        return self._backend_count

    def print_child_backend(self):
        return pc.console_log(self._backend_count)


class GrandchildState(ChildState):


    def increment_grandchild_backend(self):
        self._backend_count += 1


    @pc.var
    def grandchild_backend(self):
        return self._backend_count


    def print_grandchild_backend(self):
        return pc.console_log(self._backend_count)


def index():
    return pc.box(
        pc.hstack(
            pc.vstack(
                pc.button("Increment Parent Backend",
                        on_click=ParentState.increment_parent_backend),
                pc.text("Parent Backend Count: ", ParentState.parent_backend),
                pc.button("Print Parent Backend",
                        on_click=ParentState.print_parent_backend)

            ),
            pc.vstack(
                pc.button("Increment Child Backend",
                        on_click=ChildState.increment_child_backend),
                pc.text("Child Backend Count: ", ChildState.child_backend),
                pc.button("Print Child Backend",
                        on_click=ChildState.print_child_backend),
            ),
            pc.vstack(
                pc.button("Increment Grandchild Backend",
                        on_click=GrandchildState.increment_grandchild_backend),
                pc.text("Child Backend Count: ", GrandchildState.grandchild_backend),
                pc.button("Print Grandchild Backend",
                        on_click=GrandchildState.print_grandchild_backend),
            ),
        )
    )  

app = pc.App(state=ParentState)
app.add_page(index)
app.compile()